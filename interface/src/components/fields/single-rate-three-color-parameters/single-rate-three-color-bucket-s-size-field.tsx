import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { SingleRateThreeColorParameterFieldProps } from './single-rate-three-color-parameters';

export function SingleRateThreeColorBucketSSizeField(props: SingleRateThreeColorParameterFieldProps): ReactElement {
  const { singleRateThreeColorParameters, setSingleRateThreeColorParameters } = props;

  const singleRateThreeColorBucketSSize = useMemo(() => {
    return singleRateThreeColorParameters.bucketS_size || '';
  }, [singleRateThreeColorParameters]);

  const setSingleRateThreeColorBucketSSize = useSetNfvTeFunctionParameter('bucketS_size', setSingleRateThreeColorParameters);
  const onSingleRateThreeColorBucketSSizeChangeHandler = useChangeHandler(setSingleRateThreeColorBucketSSize);

  return (
    <FormInput
      label="Quantidade Inicial de Tokens no Bucket E"
      name="bucket-s-size"
      value={singleRateThreeColorBucketSSize}
      onChange={onSingleRateThreeColorBucketSSizeChangeHandler}
    />
  );
}
