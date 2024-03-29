import React, { ReactElement, useEffect } from 'react';
import { StateUpdater } from '@/commons/change-handler';
import { useNfvTeFunctionParameters } from '@/commons/nfv-te-values';
import { LeakyBucketIntervalField } from './leaky-bucket-interval-field';
import { LeakyBucketMaxSizeField } from './leaky-bucket-max-size-field';
import { LeakyBucketPacketsToReleaseField } from './leaky-bucket-packets-to-release-field';

type LeakyBucketParameters = {
  packets_to_release: string,
  bucket_max_size: string,
  interval: string,
};

export function LeakyBucketParameters(): ReactElement {
  const [leakyBucketParameters, setLeakyBucketParameters] = useNfvTeFunctionParameters<LeakyBucketParameters>();

  useSetLeakyBucketInitialParameters(setLeakyBucketParameters);

  return (
    <>
      <LeakyBucketIntervalField
        leakyBucketParameters={leakyBucketParameters}
        setLeakyBucketParameters={setLeakyBucketParameters}
      />

      <LeakyBucketMaxSizeField
        leakyBucketParameters={leakyBucketParameters}
        setLeakyBucketParameters={setLeakyBucketParameters}
      />

      <LeakyBucketPacketsToReleaseField
        leakyBucketParameters={leakyBucketParameters}
        setLeakyBucketParameters={setLeakyBucketParameters}
      />
    </>
  );
}

export interface LeakyBucketParameterFieldProps {
  leakyBucketParameters: LeakyBucketParameters,
  setLeakyBucketParameters: StateUpdater<LeakyBucketParameters>,
}

function useSetLeakyBucketInitialParameters(setLeakyBucketParameters: StateUpdater<LeakyBucketParameters>): void {
  useEffect(() => {
    setLeakyBucketParameters({
      packets_to_release: '',
      bucket_max_size: '',
      interval: '',
    });
  }, [setLeakyBucketParameters]);
}
