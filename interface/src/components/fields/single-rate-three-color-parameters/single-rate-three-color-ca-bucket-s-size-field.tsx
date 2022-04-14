import React, { ReactElement, useMemo } from 'react';
import { useSetNfvTeFunctionParameter } from '@/commons/nfv-te-values';
import { useChangeHandler } from '@/commons/change-handler';
import { FormInput } from '../../form-input';
import { SingleRateThreeColorParameterFieldProps } from './single-rate-three-color-parameters';

export function SingleRateThreeColorCaBucketSSizeField(props: SingleRateThreeColorParameterFieldProps): ReactElement {
  const { singleRateThreeColorParameters, setSingleRateThreeColorParameters } = props;

  const singleRateThreeColorCaBucketSSize = useMemo(() => {
    return singleRateThreeColorParameters.ca_bucketS_size || '';
  }, [singleRateThreeColorParameters]);

  const setSingleRateThreeColorBucketSSize = useSetNfvTeFunctionParameter('ca_bucketS_size', setSingleRateThreeColorParameters);
  const onSingleRateThreeColorBucketSSizeChangeHandler = useChangeHandler(setSingleRateThreeColorBucketSSize);

  return (
    <FormInput
      label="Quantidade Inicial de Tokens no Bucket E do Color Aware"
      name="ca-bucket-s-size"
      value={singleRateThreeColorCaBucketSSize}
      onChange={onSingleRateThreeColorBucketSSizeChangeHandler}
    />
  );
}
